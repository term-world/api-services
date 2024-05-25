import sys
sys.path.append('/Users/bergasanargya/summer_research_AC/term-util/libs')  # Add the libs directory

print("Python path:")
for path in sys.path:
    print(path)

try:
    from inventory.Inventory import Acquire
    from inventory.Item import ItemSpec
    print("Inventory import successful")
except ImportError as e:
    print(f"Inventory import error: {e}")
