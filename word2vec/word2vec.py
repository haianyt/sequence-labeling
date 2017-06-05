import math
import helper
import numpy as np
import tensorflow as tf

embedding_matrix = helper.getEmbedding('./word_embedding')
embedding_var = tf.Variable(embedding_matrix, trainable=False, name="emb", dtype=tf.float32)
saver = tf.train.Saver()
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    saver.save(sess, "model.ckpt")

print('finish')