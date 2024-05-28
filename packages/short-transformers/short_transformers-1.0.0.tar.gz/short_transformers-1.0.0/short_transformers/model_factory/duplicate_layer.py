import torch
import torch.nn as nn

from transformers import AutoModelForCausalLM, AutoTokenizer
import copy

def get_model(model_name: str, duplicate_layer: int, device="cuda"):

    model = AutoModelForCausalLM.from_pretrained(
        model_name, output_attentions=False
    ).to(device)

    # cut one layer, duplicate another
    new_layers = nn.ModuleList()

    for i in range(0, len(model.model.layers)):
        if i == duplicate_layer:
            # add twice = duplicate
            # todo: renaming needed
            layer = model.model.layers[i]
            layer_cloned = copy.deepcopy(layer)
            new_layers.append(layer)
            new_layers.append(layer_cloned)            
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
        f"{model.config._name_or_path}-duplicated_{duplicate_layer}"
    )
    model.config.num_hidden_layers = changed_num_hidden_layers
    model.config._name_or_path = changed_model_name_or_path
    return model

if __name__ == "__main__":

    model_name = "mistralai/Mistral-7B-v0.1"
    cut_layer = 3
    duplicate_layer = 26

    model = get_caterpillar_model(model_name, cut_layer=cut_layer, duplicate_layer=duplicate_layer).to("cuda")

    print("CATERPILLAR_MODEL")
    print(model)

    # try prediction
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    sample = tokenizer(
        "This is a sample string.",
        return_tensors="pt",
        padding=False,
        truncation=False,
    ).to("cuda")

    out = model(**sample)