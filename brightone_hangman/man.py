"""
A poor man whose job is to hang on the noose.
"""


class Man:
    limb_chars = {
        'head':      'o',
        'left_arm':  '/',
        'torso_upper': '|',
        'right_arm': '\\',
        'torso_lower': '|',
        'left_leg': '/',
        'right_leg': '\\'
    }

    def __init__(self):
        self.limbs = {
            'head':      '',
            'left_arm':  '',
            'torso_upper': '',
            'right_arm': '',
            'torso_lower': '',
            'left_leg': '',
            'right_leg': ''
        }

    def add_limb(self):
        for name, value in self.limbs.items():
            if not value:
                self.limbs[name] = self.limb_chars[name]
                return 1
        else:
            return 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        l = self.limbs
        return f'''   ____
  |    |
  |    {l["head"]}
  |   {l["left_arm"]}{l["torso_upper"]}{l["right_arm"]}
  |    {l["torso_lower"]}
  |   {l["left_leg"]} {l["right_leg"]}
 _|_
|   |________
|            |
|____________|'''
