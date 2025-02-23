import streamlit as st
import csv
import os

# Display the feedback form
st.title("Chatbot Feedback Form")
st.write("Please share your experience with our chatbot.")

# Collect user information
name = st.text_input("Your Name")
email = st.text_input("Your Email")

# Collect feedback about the chatbot
rating = st.slider("Rate your overall experience with the chatbot (0 = Poor, 10 = Excellent)", 0, 10)
ease_of_use = st.slider("How easy was it to use the chatbot? (0 = Very Difficult, 10 = Very Easy)", 0, 10)

features_liked = st.text_area("What features or aspects of the chatbot did you like the most?")
preferred_features = st.text_area("What additional features would you like to see in the chatbot?")

recommendation = st.radio("Would you recommend this chatbot to others?", options=["Yes", "No"])
return_usage = st.radio("Would you use this chatbot again?", options=["Yes", "No"])

# Submit button
if st.button("Submit Feedback"):
    # Show appropriate response based on rating
    if rating >= 8:
        st.success(f"Thank you, {name}! We're glad you had a great experience! 😊")
    elif rating <= 4:
        st.warning(f"Sorry to hear that, {name}. We’ll work on improving the chatbot. 😔")
    else:
        st.info("Thank you for your feedback!")

    # Save feedback to a CSV file
    file_name = "chatbot_feedback.csv"
    file_exists = os.path.isfile(file_name)
    try:
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write header if file doesn't exist
                writer.writerow([ 
                    "Name", "Email", "Rating", "Ease of Use",
                    "Features Liked", "Preferred Features",
                    "Recommendation", "Return Usage",
                ])
            # Write user feedback
            writer.writerow([ 
                name, email, rating, ease_of_use,
                features_liked, preferred_features,
                recommendation, return_usage,
            ])
        st.success("Your feedback has been successfully saved!")
    except Exception as e:
        st.error(f"An error occurred while saving your feedback: {e}")
