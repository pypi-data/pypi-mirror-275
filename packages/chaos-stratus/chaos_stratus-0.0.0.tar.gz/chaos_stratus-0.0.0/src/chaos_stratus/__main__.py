import sys
from stratus import Effect

if __name__ == '__main__':
    lib = sys.argv[1]
    effect = Effect(lib)
    print(f'Stratus effect library {lib}:')
    print(f'  Effect name:....... {effect.name}')
    print(f'  Effect ID:......... {effect.effectId}')
    print(f'  Effect version:.... {effect.version}')
    print(f'  Number of knobs:... {effect.knobCount}')
    print(f'  Number of switches: {effect.switchCount}')
