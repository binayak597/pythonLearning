from typing import List, Tuple, Dict, Union


# traditional way
age = 45

# using type definition

age: int = 45

print(age)


name: str = "Binayak"

# list that only contain integers
l: List[int] = [1, 2, 3, 4, 5]

# tuple that contain integer and string values

t: Tuple[str, int] = (1, "binayak", "ramesh", 45)

# dict that contain {str: int} values

d: Dict[str, int] = {"mark": 40, "math": 95}

# union types of variable that contain multiple types of data combinely

u: Union[str, int] = "ID123"



