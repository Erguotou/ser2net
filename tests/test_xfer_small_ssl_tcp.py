#!/usr/bin/python

import gensio
from dataxfer import test_transfer
import utils

rb = gensio.get_random_bytes(512)

test_transfer("ssl tcp small random", rb,
              "ssl(key=%s/key.pem,cert=%s/cert.pem),3023:raw:100:/dev/ttyPipeA0:9600N81\n" % (utils.keydir, utils.keydir),
              "ssl(CA=%s/CA.pem),tcp,localhost,3023" % utils.keydir,
              "serialdev,/dev/ttyPipeB0,9600N81",
              timeout=5000)
