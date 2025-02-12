    import tensorflow as tf
     
    mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    X_train, x_test = x_train / 255.0, x_test / 255.0
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
    model.compile(optimizer=tf.optimizers.Adam(),
                  loss=’sparse_categorical_crossentropy’,
                  metrics=[‘accuracy’])
    model.fit(x_train, y_train, epochs=10)