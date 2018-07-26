    Y=test[b'data'][idx].reshape(32,32,3)
    YY = np.stack([Y.reshape(3,32,32)[0],
               Y.reshape(3,32,32)[1],
               Y.reshape(3,32,32)[2]],
               axis=2)

