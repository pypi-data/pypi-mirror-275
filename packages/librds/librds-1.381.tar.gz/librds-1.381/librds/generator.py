from .group import Group
from .comfort import get_from_list
from .af import AlternativeFrequency
from .charset import RDSCharset

class GroupGenerator:
    def basic(pi:int, tp: bool=False, pty: int=0):
        """This function will generate a basic block structure which includes the PI, TP and PTY, this shouldn't be sent by itself to a decoder"""
        return Group(
            pi & 0xFFFF, #A
            (int(tp) << 10 | pty << 5) & 0xFFFF, #B
            0,0, #C
            None #is_b
        )
    def ps(blocks:Group,ps_text:str,segment:int,ms:bool=True,ta:bool=False,di:int=1,block2:int=0):
        """This function will generate a 0A group which includes TA MS DI AF and text data"""
        if segment > 3: raise Exception("Segment limit")
        return Group(
            blocks.a & 0xFFFF,
            ( blocks.b | int(ta) << 4 | int(ms) << 3 | ( ( di >> (3-segment) ) << 2) | segment ) & 0xFFFF,
            int(block2) & 0xFFFF or AlternativeFrequency.get_no_af(),
            (RDSCharset.translate(get_from_list(ps_text,segment*2," "))<<8 | RDSCharset.translate(get_from_list(ps_text,segment*2+1," "))) & 0xFFFF, #low byte + high byte as we're using utf-8, and we conver 2 8 bit numbers to a single 16 bit one
            False
        )
    def ps_b(blocks:Group,ps_text:str,segment:int,ms:bool=True,ta:bool=False,di:int=1):
        """This function will generate a 0B group which is very similiar to a 0A group but no AF"""
        if segment > 3: raise Exception("Segment limit")
        return Group(
            blocks.a & 0xFFFF,
            ( blocks.b | int(ta) << 4 | int(ms) << 3 | ( ( di >> (3-segment) ) << 2) | segment ) & 0xFFFF,
            blocks.a & 0xFFFF,
            (RDSCharset.translate(get_from_list(ps_text,segment*2," "))<<8 | RDSCharset.translate(get_from_list(ps_text,segment*2+1," "))) & 0xFFFF,
            True
        )
    def ecc(blocks:Group, ecc: int):
        """This function will generate a 1A group"""
        return Group(
            blocks.a & 0xFFFF,
            (blocks.b | 1 << 12) & 0xFFFF,
            (blocks.c | ecc) & 0xFFFF,
            blocks.d & 0xFFFF,
            False
        )
    def lic(blocks:Group, lic: int):
        """This function will generate a 1A group"""
        return Group(
            blocks.a & 0xFFFF,
            (blocks.b | 1 << 12) & 0xFFFF,
            (blocks.c | (lic | 0x3000)) & 0xFFFF,
            blocks.d & 0xFFFF,
            False
        )
    def rt(blocks:Group,rt_text:str,segment:int,ab:bool=False):
        """This function will generate a 2A group"""
        if segment > 15: raise Exception("Segment limit")
        return Group(
            blocks.a & 0xFFFF,
            (blocks.b | 2 << 12 | int(ab) << 4 | segment) & 0xFFFF,
            (RDSCharset.translate(get_from_list(rt_text,segment*4+0," "))<<8 | RDSCharset.translate(get_from_list(rt_text,segment*4+1," "))) & 0xFFFF,
            (RDSCharset.translate(get_from_list(rt_text,segment*4+2," "))<<8 | RDSCharset.translate(get_from_list(rt_text,segment*4+3," "))) & 0xFFFF,
            False
        )
    def rt_b(blocks:Group,rt_text:str,segment:int,ab:bool=False):
        """This function will generate a 2B group"""
        if segment > 15: raise Exception("Segment limit")
        return Group(
            blocks.a & 0xFFFF,
            (0x0800 | blocks.a | 2 << 12 | int(ab) << 4 | segment) & 0xFFFF,
            blocks.a & 0xFFFF,
            (RDSCharset.translate(get_from_list(rt_text,segment*4+0," "))<<8 | RDSCharset.translate(get_from_list(rt_text,segment*4+1," "))) & 0xFFFF,
            True
        )
    def tda(blocks:Group, channel:int,data:list[int],segment:int):
        """This function will generate a 5A group"""
        return Group(
            blocks.a & 0xFFFF,
            (blocks.b | 5 << 12 | (channel & 0x001F)) & 0xFFFF,
            (get_from_list(data,segment+0,0)<<8 | get_from_list(data,segment+1,0)) & 0xFFFF,
            (get_from_list(data,segment+2,0)<<8 | get_from_list(data,segment+3,0)) & 0xFFFF,
            False
        )
    def tda_b(blocks:Group, channel:int,data:list[int],segment:int):
        """This function will generate a 5B group"""
        return Group(
            blocks.a & 0xFFFF,
            (0x0800 | blocks.b | 5 << 12 | (channel & 0x001F)) & 0xFFFF,
            blocks.a & 0xFFFF,
            (get_from_list(data,segment+0,0)<<8 | get_from_list(data,segment+1,0)) & 0xFFFF,
            True
        )
    def in_house(blocks:Group, data:list[int]):
        """This function will generate a 6A group"""
        return Group(
            blocks.a & 0xFFFF,
            (((blocks.b | 6 << 12) & ~0b11111) | (get_from_list(data,0,0) & 0b11111)) & 0xFFFF,
            get_from_list(data,1,0) & 0xFFFF,
            get_from_list(data,2,0) & 0xFFFF,
            False
        )
    def in_house_b(blocks:Group, data:list[int]):
        """This function will generate a 6B group"""
        return Group(
            blocks.a & 0xFFFF,
            (((0x0800 | blocks.b | 6 << 12) & ~0b11111) | (get_from_list(data,0,0) & 0b11111)) & 0xFFFF,
            blocks.a & 0xFFFF,
            get_from_list(data,1,0) & 0xFFFF,
            True
        )
    def ptyn(blocks:Group, ptyn_text:str, segment:int,ab:bool=False):
        """This function will generate a 10A group"""
        if segment > 1: raise Exception("Segment limit")
        return Group(
            blocks.a & 0xFFFF,
            (blocks.b | 10 << 12 | (int(ab) << 4) | segment) & 0xFFFF,
            (RDSCharset.translate(get_from_list(ptyn_text,segment*4+0," "))<<8 | RDSCharset.translate(get_from_list(ptyn_text,segment*4+1," "))) & 0xFFFF,
            (RDSCharset.translate(get_from_list(ptyn_text,segment*4+2," "))<<8 | RDSCharset.translate(get_from_list(ptyn_text,segment*4+3," "))) & 0xFFFF,
            False
        )
