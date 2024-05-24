import imageio

# 读取 GIF 文件
im = imageio.mimread('/home/qsliu/Documents/DNA-SE/package/DNA_SE/training_loss_convergence2.gif')

# 设置更快的帧率
imageio.mimsave('output.gif', im, duration=0.05)