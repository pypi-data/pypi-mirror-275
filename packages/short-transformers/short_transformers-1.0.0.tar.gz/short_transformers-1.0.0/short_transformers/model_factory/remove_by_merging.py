import torch
import torch.nn as nn

from transformers import AutoModelForCausalLM, AutoTokenizer
import copy

def merge_layers(layerA, layerB):

    sdA = layerA.state_dict()
    sdB = layerB.state_dict()

    # Average all parameters
    for key in sdA:
        sdB[key] = (sdB[key] + sdA[key]) / 2.

    # Load averaged state_dict
    layerC = copy.deepcopy(layerA)
    layerC.load_state_dict(sdB)

    return layerC

# def merge_layers(layers, weights = None):
#     # @TODO check it
#     state_dicts = [layer.state_dict() for layer in layers]
#     first_state_dict = state_dicts[0]

#     for key in first_state_dict:
#         meta = [state_dict[key] for state_dict in state_dicts]
#         if weights:
#             first_state_dict[key] = (meta@weights)/meta.sum()
#         else:
#             first_state_dict[key] = sum(meta)/len(meta) 
        
#     avg_layer = copy.deepcopy(layers[0])
#     avg_layer.load_state_dict(first_state_dict)
#     return avg_layer

# def merge_layers(
#     tensors: torch.Tensor, **_kwargs
# ) -> torch.Tensor:
#     keys = list(tensors.keys())

#     tensors = [tensors[key] for key in keys]
#     weights = [self.tensor_parameters[key]["weight"] for key in keys]

#     rectify_embed_sizes(self.weight_info, tensors)

#     unique_shapes = set(t.shape for t in tensors)
#     if len(unique_shapes) != 1:
#         raise RuntimeError(
#             f"Tensor size mismatch for {self.weight_info.name}, sizes: {list(unique_shapes)}"
#         )

#     tensors = torch.stack(tensors, dim=0)
#     weights = torch.tensor(weights, dtype=tensors.dtype, device=tensors.device)
#     while len(weights.shape) < len(tensors.shape):
#         weights.unsqueeze_(-1)

#     res = (weights * tensors).sum(dim=0)
#     if self.normalize:
#         res = res / weights.sum(dim=0)

#     return res

# @TODO merge with next or prev, currently only prev is supported
def get_model(model_name: str, merge_idx: int, device="cuda"):

    model = AutoModelForCausalLM.from_pretrained(
        model_name, output_attentions=False, device_map="auto"
    )#.to(device)
    print(model)

    # cut one layer, duplicate another
    new_layers = nn.ModuleList()

    for i in range(0, len(model.model.layers)):
        if i == merge_idx:
            # merge with previous
            prev_layer = new_layers[-1]
            avg_layer = merge_layers(model.model.layers[i], prev_layer)
            # overwrite prev layer
            new_layers[-1] = avg_layer       
        else:
            layer = model.model.layers[i]
            new_layers.append(layer)

    model.model.layers = new_layers

    # rename layers
    # not sure how universal is this
    for i, layer in enumerate(model.model.layers):
        layer.self_attn.layer_idx = i

    changed_num_hidden_layers = len(model.model.layers)
    changed_model_name_or_path = (
        f"{model.config._name_or_path}-merged_{merge_idx}"
    )
    model.config.num_hidden_layers = changed_num_hidden_layers
    model.config._name_or_path = changed_model_name_or_path
    return model

if __name__ == "__main__":

    for i in range(12, 20):

        model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
        sanitized_model_name = model_name.split("/")[-1]
        merge_idx=i
        device = "cuda"
        model = get_model(model_name, merge_idx=merge_idx, device=device)

        print("CUT_BY_MERGE_MODEL")
        print(model)

        # try prediction
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # sample = tokenizer(
        #     "You should never cut layers of your model",
        #     return_tensors="pt",
        #     padding=False,
        #     truncation=False,
        # ).to(device)

        # out = model(**sample)

        print("saving the model")
        model.save_pretrained(model.config._name_or_path, save_safetensors=False)
        tokenizer.save_pretrained(model.config._name_or_path)
        print("finished the same")
        # model.push_to_hub(f"melisa/{sanitized_model_name}_merged_{i}")
        # tokenizer.push_to_hub(f"melisa/{sanitized_model_name}_merged_{i}")

        del model
        import gc
        gc.collect()
        torch.cuda.empty_cache()
