questions = ("You find yourself wandering through an ethereal, glowing forest, the trees whispering secrets of old. In a clearing, a wise old oak poses a question to you: 'What force guides your journey through the twisting paths of life?'",
                       "Floating amidst the cosmos on a platform of stardust, you gaze upon the infinite. A celestial being appears before you, its eyes reflecting nebulae, and inquires: 'What do you hope to discover in the vast expanse of your soul's universe?'",
                       "Surrounded by books that contain the wisdom of the ages, a shadowy figure, the keeper of knowledge, asks you: 'What chapters of your life do you find yourself revisiting, and what lessons do they hold?'",
                       "Submerged in the deep blue, surrounded by the dance of light and shadow, a mermaid queen emerges to ask: 'In the currents of your deepest thoughts, what treasures do you seek?'",
                       "Standing at the peak, where the sky kisses the earth, a voice carried by the wind asks: 'As you gaze upon the horizon of your future, what do you see taking shape in the clouds of possibility?'"
")

options = (("A. The pursuit of knowledge and wisdom, always seeking to understand more.", "B. The quest for emotional fulfillment and meaningful connections.", "C. The drive to overcome challenges and achieve personal milestones.", "D. The desire for tranquility, harmony, and alignment with nature."),
                   ("A. Uncharted territories of my potential and capabilities.", "B. Deep, hidden emotions and untold stories of my heart.", "C. The eternal truths and philosophies that govern existence.", "D. The serene quietude that comes from cosmic acceptance and understanding."),
                   ("A. Times of great change, reminding me of the impermanence of life.", "B. Moments of joy and sorrow, teaching me the depth of human emotion.", "C. Periods of solitude, revealing the value of self-reflection and growth.", "D. Instances of conflict and resolution, illustrating the power of empathy and understanding."),
                   ("A. The pearl of true purpose, giving direction to my endeavors.", "B. The coral of hidden strengths, waiting to be discovered and nurtured.", "C. The sunken ship of forgotten dreams, ready to be salvaged and pursued anew.", "D. The ancient ruins of past civilizations, offering insights and wisdom for the future."),
                   ("A. Towers of achievement and recognition, built upon the foundations of hard work and dedication.", "B. Gardens of relationships and community, flourishing with love and mutual support.", "C. Rivers of adventure and discovery, meandering through landscapes of the unknown.", "D. Sanctuaries of peace and solitude, nestled in valleys of contentment and self-fulfillment."))


guesses = []
score = 0
question_num = 0

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")