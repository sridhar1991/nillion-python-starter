from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    factor = SecretInteger(Input(name="factor", party=party1))
    number_mod=my_int1%factor
    evencondition=number_mod>=Integer(1)
    result=evencondition.if_else(
      Integer(0),Integer(1)
    )
    return [Output(result, "Is_Even", party1)]