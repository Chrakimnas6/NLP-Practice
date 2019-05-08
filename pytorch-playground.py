import torch
x = torch.tensor([[5.5, 3]]) # x.size() is tuple ex.[1,2] 1 row 2 columns
# print(x.size())
x = torch.rand(5, 3)
y = torch.rand(5, 3)
# print(x,"\n", y, "\n", x + y) 
# print(x, x[:,1]) # get the second coloum
x = torch.randn(4, 4)
y = x.view(16) # turn the size to [16]
z = x.view(-1, 8) # size [2, 8]
# print(x.size(), "\n", y.size(), "\n", z.size())
# print(x.item()) # only one element tensors can be converted to Python scalar

#a = torch.ones(5)
#b = a.numpy()
#print(a, b)
#a.add_(1) # underline means in-place
#print(a, b) # Torch Tensor and NumPy array will share their underlying memory locations

x = torch.ones(2, 2, requires_grad=True) # starts to track all aperations on x
print(x)
y = x + 2
print(y)
print(y.grad_fn)
z = y * y * 3
out = z.mean()
#print(z)
#print(out)
out.backward() # to have all the gradients computed automatically
print(x.grad) # the gradient for this tensor will be accumulated
# zi = 3(xi+2)^2, differentiate it will get 3/2 (xi+2)
