import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import konlpy
from konlpy.corpus import kolaw
print(kolaw.open('constitution.txt').read()[:20])