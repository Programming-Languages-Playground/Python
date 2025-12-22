import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()
brewing_time.to("Canada/Toronto")

chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
