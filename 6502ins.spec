0x00 BRK # 2
0x01 ORA (zp,x) 2
0x02 INVL INV 1
0x03 INVL INV 1
0x04 TSB zp 2
0x05 ORA zp 2
0x06 ASL zp 2
0x07 RMB0 zp 2
0x08 PHP s 1
0x09 ORA # 2
0x0a ASL A 1
0x0b INVL INV 1
0x0c TSB a 3
0x0d ORA a 3
0x0e ASL a 3
0x0f BBR0 r 2
0x10 BPL r 2
0x11 ORA (zp),y 2
0x12 ORA (zp) 2
0x13 INVL INV 1
0x14 TRB zp 2
0x15 ORA zp,x 2
0x16 ASL zp,x 2
0x17 RMB1 zp 2
0x18 CLC i 1
0x19 ORA a,y 3
0x1a INC A 1
0x1b INVL INV 1
0x1c TRB a 3
0x1d ORA a,x 3
0x1e ASL a,x 3
0x1f BBR1 r 2
0x20 JSR a 3
0x21 AND (zp,x) 2
0x22 INVL INV 1
0x23 INVL INV 1
0x24 BIT zp 2
0x25 AND zp 2
0x26 ROL zp 2
0x27 RMB2 zp 2
0x28 PLP s 1
0x29 AND # 2
0x2a ROL A 1
0x2b INVL INV 1
0x2c BIT a 3
0x2d AND a 3
0x2e ROL a 3
0x2f BBR2 r 2
0x30 BMI r 2
0x31 AND (zp),y 2
0x32 AND (zp) 2
0x33 INVL INV 1
0x34 BIT zp,x 2
0x35 AND zp,x 2
0x36 ROL zp,x 2
0x37 RMB3 zp 2
0x38 SEC i 1
0x39 AND a,y 3
0x3a DEC A 1
0x3b INVL INV 1
0x3c BIT a,x 3
0x3d AND a,x 3
0x3e ROL a,x 3
0x3f BBR3 r 2
0x40 RTI s 1
0x41 EOR (zp,x) 2
0x42 INVL INV 1
0x43 INVL INV 1
0x44 INVL INV 1
0x45 EOR zp 2
0x46 LSR zp 2
0x47 RMB4 zp 2
0x48 PHA s 1
0x49 EOR # 2
0x4a LSR A 1
0x4b INVL INV 1
0x4c JMP a 3
0x4d EOR a 3
0x4e LSR a 3
0x4f BBR4 r 2
0x50 BVC r 2
0x51 EOR (zp),y 2
0x52 EOR (zp) 2
0x53 INVL INV 1
0x54 INVL INV 1
0x55 EOR zp,x 2
0x56 LSR zp,x 2
0x57 RMB5 zp 2
0x58 CLI i 1
0x59 EOR a,y 3
0x5a PHY s 1
0x5b INVL INV 1
0x5c INVL INV 1
0x5d EOR a,x 3
0x5e LSR a,x 3
0x5f BBR5 r 2
0x60 RTS s 1
0x61 ADC (zp,x) 2
0x62 INVL INV 1
0x63 INVL INV 1
0x64 STZ zp 2
0x65 ADC zp 2
0x66 ROR zp 2
0x67 RMB6 zp 2
0x68 PLA s 1
0x69 ADC # 2
0x6a ROR A 1
0x6b INVL INV 1
0x6c JMP (a) 3
0x6d ADC a 3
0x6e ROR a 3
0x6f BBR6 r 2
0x70 BVS r 2
0x71 ADC (zp),y 2
0x72 ADC (zp) 2
0x73 INVL INV 1
0x74 STZ zp,x 2
0x75 ADC zp,x 2
0x76 ROR zp,x 2
0x77 RMB7 zp 2
0x78 SEI i 1
0x79 ADC a,y 3
0x7a PLY s 1
0x7b INVL INV 1
0x7c JMP (a,x) 3
0x7d ADC a,x 3
0x7e ROR a,x 3
0x7f BBR7 r 2
0x80 BRA r 2
0x81 STA (zp,x) 2
0x82 INVL INV 1
0x83 INVL INV 1
0x84 STY zp 2
0x85 STA zp 2
0x86 STX zp 2
0x87 SMB0 zp 2
0x88 DEY i 1
0x89 BIT # 2
0x8a TXA i 1
0x8b INVL INV 1
0x8c STY a 3
0x8d STA a 3
0x8e STX a 3
0x8f BBS0 r 2
0x90 BCC r 2
0x91 STA (zp),y 2
0x92 STA (zp) 2
0x93 INVL INV 1
0x94 STY zp,x 2
0x95 STA zp,x 2
0x96 STX zp,y 2
0x97 SMB1 zp 2
0x98 TYA i 1
0x99 STA a,y 3
0x9a TXS i 1
0x9b INVL INV 1
0x9c STZ a 3
0x9d STA a,x 3
0x9e STZ a,x 3
0x9f BBS1 r 2
0xa0 LDY # 2
0xa1 LDA (zp,x) 2
0xa2 LDX # 2
0xa3 INVL INV 1
0xa4 LDY zp 2
0xa5 LDA zp 2
0xa6 LDX zp 2
0xa7 SMB2 zp 2
0xa8 TAY i 1
0xa9 LDA # 2
0xaa TAX i 1
0xab INVL INV 1
0xac LDY a 3
0xad LDA a 3
0xae LDX a 3
0xaf BBS2 r 2
0xb0 BCS r 2
0xb1 LDA (zp),y 2
0xb2 LDA (zp) 2
0xb3 INVL INV 1
0xb4 LDY zp,x 2
0xb5 LDA zp,x 2
0xb6 LDX zp,y 2
0xb7 SMB3 zp 2
0xb8 CLV i 1
0xb9 LDA a,y 3
0xba TSX i 1
0xbb INVL INV 1
0xbc LDY a,x 3
0xbd LDA a,x 3
0xbe LDX a,y 3
0xbf BBS3 r 2
0xc0 CPY # 2
0xc1 CMP (zp,x) 2
0xc2 INVL INV 1
0xc3 INVL INV 1
0xc4 CPY zp 2
0xc5 CMP zp 2
0xc6 DEC zp 2
0xc7 SMB4 zp 2
0xc8 INY i 1
0xc9 CMP # 2
0xca DEX i 1
0xcb WAI i 1
0xcc CPY a 3
0xcd CMP a 3
0xce DEC a 3
0xcf BBS4 r 2
0xd0 BNE r 2
0xd1 CMP (zp),y 2
0xd2 CMP (zp) 2
0xd3 INVL INV 1
0xd4 INVL INV 1
0xd5 CMP zp,x 2
0xd6 DEC zp,x 2
0xd7 SMB5 zp 2
0xd8 CLD i 1
0xd9 CMP a,y 3
0xda PHX s 1
0xdb STP i 1
0xdc CMP a,x 3
0xdd INVL INV 1
0xde DEC a,x 3
0xdf BBS5 r 2
0xe0 CPX # 2
0xe1 SBC (zp,x) 2
0xe2 INVL INV 1
0xe3 INVL INV 1
0xe4 CPX zp 2
0xe5 SBC zp 2
0xe6 INC zp 2
0xe7 SMB6 zp 2
0xe8 INX i 1
0xe9 SBC # 2
0xea NOP i 1
0xeb CPX a 3
0xec INVL INV 1
0xed SBC a 3
0xee INC a 3
0xef BBS6 r 2
0xf0 BEQ r 2
0xf1 SBC (zp),y 2
0xf2 SBC (zp) 2
0xf3 INVL INV 1
0xf4 INVL INV 1
0xf5 SBC zp,x 2
0xf6 INC zp,x 2
0xf7 SMB7 zp 2
0xf8 SED i 1
0xf9 SBC a,y 3
0xfa PLX s 1
0xfb SBC a,x 3
0xfc INVL INV 1
0xfd INVL INV 1
0xfe INC a,x 3
0xff BBS7 r 2
