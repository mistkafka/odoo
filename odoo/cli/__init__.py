import logging
import sys
import os

import odoo

from .command import Command, main

from . import deploy  # 我觉得这个命令需要看看，用来安装插件的。
from . import scaffold
from . import server
from . import shell
from . import start
