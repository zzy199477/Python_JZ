
Constant1 = 1.371
Constant2 = 0.371

dictCoefficients = {'Vision':             [1,0.98,0.89,0.84,0.75,0.61],
                    'Hearing':            [1,0.95,0.89,0.8,0.74,0.61],
                    'Speech':             [1,0.94,0.89,0.81,0.68],
                    'Ambulation':         [1,0.93,0.86,0.73,0.65,0.58],
                    'Dexterity':          [1,0.95,0.88,0.76,0.65,0.56],
                    'Emotion':            [1, 0.95, 0.85, 0.64, 0.46],
                    'Cognition':          [1, 0.92, 0.95, 0.83, 0.6, 0.42],
                    'Pain':               [1, 0.96, 0.9, 0.77, 0.55]};

def get_score(Vision, Hearing, Speech, Ambulation, Dexterity, Emotion, Cognition, Pain):

    if not (Vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5 or 6')
    if not (Hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5 or 6')
    if not (Speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4 or 5')
    if not (Ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5 or 6')
    if not (Dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5 or 6')
    if not (Emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4 or 5')
    if not (Cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5 or 6')
    if not (Pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4 or 5')

    Vision = dictCoefficients['Vision'][Vision-1]
    Hearing = dictCoefficients['Hearing'][Hearing - 1]
    Speech = dictCoefficients['Speech'][Speech - 1]
    Ambulation = dictCoefficients['Ambulation'][Ambulation - 1]
    Dexterity = dictCoefficients['Dexterity'][Dexterity - 1]
    Emotion = dictCoefficients['Emotion'][Emotion - 1]
    Cognition = dictCoefficients['Cognition'][Cognition - 1]
    Pain = dictCoefficients['Pain'][Pain - 1]

    score = Constant1*(Vision*Hearing*Speech*Ambulation*Dexterity*Emotion*Cognition*Pain)-Constant2

    return score