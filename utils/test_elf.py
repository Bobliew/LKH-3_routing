import elftools
from elftools.elf.elffile import ELFFile
#from capstone import Cs, CS_ARCH_X86, CS_MODE_64



# 打开 LKH 的 ELF 文件
with open('../LKH', 'rb') as f:
    elf = ELFFile(f)

    # 解析代码段
    code_section = elf.get_section_by_name('.text')
    code_data = code_section.data()

from capstone import Cs, CS_ARCH_X86, CS_MODE_64

