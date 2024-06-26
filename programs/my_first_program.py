from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # New computation: multiply my_int1 and my_int2
    result = my_int1 * my_int2

    # make sure you change the output below to be your new output
    return [Output(result, "my_output", party1)]
