#!/usr/bin/env python3.11
ONE   = int(bool(bool))
TWO   = ONE   + ONE
THREE = TWO   + ONE
FOUR  = THREE + ONE
FIVE  = FOUR  + ONE
SIX   = FIVE  + ONE
SEVEN = SIX   + ONE
EIGHT = SEVEN + ONE

i = int()

i += TWO;   i <<= THREE
i += TWO;   i <<= THREE
i <<= THREE
i += SIX;   i <<= THREE
i += TWO;   i <<= THREE
i += FIVE;  i <<= THREE
i += FIVE;  i <<= THREE
i += FOUR;  i <<= THREE
i += THREE; i <<= THREE
i += THREE; i <<= THREE
i <<= THREE
i += SIX;   i <<= THREE
i += SEVEN; i <<= THREE
i += FOUR;  i <<= THREE
i += FOUR;  i <<= THREE
i <<= THREE
i += TWO;   i <<= THREE
i += FIVE;  i <<= THREE
i += SIX;   i <<= THREE
i += SIX;   i <<= THREE
i += SEVEN; i <<= THREE
i += FIVE;  i <<= THREE
i += SIX;   i <<= THREE
i += TWO;   i <<= THREE
i += THREE; i <<= THREE
i += THREE; i <<= THREE
i <<= THREE
i += SIX;   i <<= THREE
i += TWO;   i <<= THREE
i <<= THREE
i += FOUR;  i <<= THREE
i += ONE

string = i.to_bytes(SIX*TWO).decode()
print(string)
