# app.py

from flask import Flask, render_template

# Initialize the Flask application
# Configure Flask to use the 'frontend' directory for both templates and static files
app = Flask(__name__, template_folder='frontend', static_folder='frontend')

# --- Mock Data ---
# In a real application, this data would come from a database.
addiction_data = {
    "nicotine": {
        "title": "Nicotine (Tobacco)",
        "description": "Tobacco addiction is primarily driven by nicotine, a highly addictive stimulant. Ayurveda views this as an imbalance of Vata and Pitta doshas, leading to nervous system agitation and cravings.",
        "herbs": [
            {"name": "Ashwagandha", "use": "Helps manage stress and reduces withdrawal symptoms like anxiety."},
            {"name": "Brahmi", "use": "Improves cognitive function and calms the nervous system."},
            {"name": "Tulsi (Holy Basil)", "use": "Chewing on Tulsi leaves can help reduce the urge to smoke and detoxify the body."}
        ],
        "lifestyle": [
            "Practice 'Pranayama' (breathing exercises) like 'Nadi Shodhana' to calm the mind.",
            "Perform 'Neti' (nasal cleansing) with saline water to clear respiratory passages.",
            "Chew on fennel seeds or licorice root as a healthy substitute for tobacco."
        ]
    },
    "alcohol": {
        "title": "Alcohol",
        "description": "Alcohol dependence negatively impacts the liver and digestive system, aggravating the Pitta dosha. Ayurveda focuses on cooling the body, detoxifying the liver, and strengthening the mind.",
        "herbs": [
            {"name": "Kutki", "use": "A potent liver-protective herb that aids in detoxification."},
            {"name": "Amalaki (Amla)", "use": "Rich in Vitamin C, it helps rejuvenate the body and supports liver function."},
            {"name": "Jatamansi", "use": "A calming herb that helps stabilize the mind and reduce alcohol cravings."}
        ],
        "lifestyle": [
            "Follow a Pitta-pacifying diet: include sweet, bitter, and astringent foods.",
            "Stay hydrated with water, coconut water, and herbal teas.",
            "Practice regular meditation to build mental resilience."
        ]
    },
    "caffeine": {
        "title": "Caffeine",
        "description": "Excessive caffeine consumption can lead to Vata imbalance, causing anxiety, insomnia, and burnout. The goal is to gently reduce dependency while nourishing the nervous system.",
        "herbs": [
            {"name": "Shankhpushpi", "use": "Enhances memory and acts as a mild tranquilizer, reducing caffeine-induced anxiety."},
            {"name": "Cardamom", "use": "Helps neutralize the acidic effects of coffee and aids digestion."},
            {"name": "Ginger", "use": "Can be consumed as a tea to provide a gentle, non-caffeinated energy boost."}
        ],
        "lifestyle": [
            "Gradually replace coffee with herbal teas like ginger or tulsi tea.",
            "Ensure a regular sleep schedule to restore natural energy cycles.",
            "Engage in grounding activities like walking barefoot on grass ('earthing')."
        ]
    }
}

@app.route('/')

def home():
    """
    Renders the main page with all the de-addiction data.
    """
    return render_template('index.html', data=addiction_data)

if __name__ == '__main__':
    # Runs the app in debug mode on port 5173 to match your previous dev port.
    # In a production environment, you would use a proper web server like Gunicorn.
    app.run(debug=True, port=5173)
