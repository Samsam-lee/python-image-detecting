import mxnet

load_symbol, args, auxs = mxnet.model.load_checkpoint("model_algo_1", 000)
mod = mxnet.mod.Module(load_symbol, label_names=None, context=mxnet.cpu())
mod.data_names

# mod.bind(data_shapes=[('data', (1, 3, 640, 480))])
# mod.set_params(args, auxs)
# print(mod.data_names)
# print(mod.data_shapes)
# print(mod.output_names)
# print(mod.output_shapes)