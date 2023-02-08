from bert_logic.bertLogic import BertLogic

# Check for empty string 
def test_bertLogic_normal():
    # When
    bert = BertLogic()
    response = bert.sequenceClassification("")
    # Then
    assert response == "positive"

def test_bertLogic_long():
    # When
    bert = BertLogic()
    response = bert.sequenceClassification("Considering how common illness is, how tremendous the spiritual change that it brings, how astonishing, when the lights of health go down, the undiscovered countries that are then disclosed, what wastes and deserts of the soul a slight attack of influenza brings to light, what precipices and lawns sprinkled with bright flowers a little rise of temperature reveals, what ancient and obdurate oaks are uprooted in us in the act of sickness, how we go down into the pit of death and feel the waters of annihilation close above our heads and wake thinking to find ourselves in the presence of the angels and the harpers when we have a tooth out and come to the surface in the dentist’s arm chair and confuse his ‘Rinse the mouth—rinse the mouth’ with the greeting of the Deity stooping from the floor of Heaven to welcome us—when we think of this and infinitely more, as we are so frequently forced to think of it, it becomes strange indeed that illness has not taken its place with love, battle, and jealousy among the prime themes of literature. Considering how common illness is, how tremendous the spiritual change that it brings, how astonishing, when the lights of health go down, the undiscovered countries that are then disclosed, what wastes and deserts of the soul a slight attack of influenza brings to light, what precipices and lawns sprinkled with bright flowers a little rise of temperature reveals, what ancient and obdurate oaks are uprooted in us in the act of sickness, how we go down into the pit of death and feel the waters of annihilation close above our heads and wake thinking to find ourselves in the presence of the angels and the harpers when we have a tooth out and come to the surface in the dentist’s arm chair and confuse his ‘Rinse the mouth—rinse the mouth’ with the greeting of the Deity stooping from the floor of Heaven to welcome us—when we think of this and infinitely more, as we are so frequently forced to think of it, it becomes strange indeed that illness has not taken its place with love, battle, and jealousy among the prime themes of literature.Considering how common illness is, how tremendous the spiritual change that it brings, how astonishing, when the lights of health go down, the undiscovered countries that are then disclosed, what wastes and deserts of the soul a slight attack of influenza brings to light, what precipices and lawns sprinkled with bright flowers a little rise of temperature reveals, what ancient and obdurate oaks are uprooted in us in the act of sickness, how we go down into the pit of death and feel the waters of annihilation close above our heads and wake thinking to find ourselves in the presence of the angels and the harpers when we have a tooth out and come to the surface in the dentist’s arm chair and confuse his ‘Rinse the mouth—rinse the mouth’ with the greeting of the Deity stooping from the floor of Heaven to welcome us—when we think of this and infinitely more, as we are so frequently forced to think of it, it becomes strange indeed that illness has not taken its place with love, battle, and jealousy among the prime themes of literature.")
    # Then
    assert response == "None"

def test_bertLogic_empty():
    try:
        # When
        bert = BertLogic()
        response = bert.sequenceClassification("")
        # Then
    except:
        raise(ValueError)


