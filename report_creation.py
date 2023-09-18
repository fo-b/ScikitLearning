import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
import re

# Load your chat messages from the data file
with open('data.txt', 'r', encoding='utf-8') as file:
    messages = file.readlines()

# Preprocess the messages (remove timestamps and split into words)
def preprocess_message(message):
    # Remove timestamps (assuming timestamps are enclosed in square brackets)
    message = re.sub(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', '', message)

    # Split the message into words (tokenization)
    words = message.split()
    return ' '.join(words)  # Join the words back into a cleaned message

# Apply preprocessing to all messages
cleaned_messages = [preprocess_message(message) for message in messages]

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)  # You can adjust the number of features
X = vectorizer.fit_transform(cleaned_messages)

# Reduce dimensionality for clustering (optional but can be helpful)
# You can skip this step if you have a small dataset
svd = TruncatedSVD(n_components=100)
X_reduced = svd.fit_transform(X)

# Perform clustering (adjust the number of clusters as needed)
num_clusters = 5  # Adjust this based on the expected number of categories
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X_reduced)

# Get cluster assignments for each message
cluster_labels = kmeans.labels_

# Define keywords or phrases to match with clusters (customize as needed)
cluster_keywords = {
    0: ['positiv', 'gut', 'glücklich', 'freude', '<3', ':)', ':D', 'hypE'],
    1: ['negativ', 'schlecht', 'unglücklich', 'traurig'],
    2: ['neutral', 'neutral', 'okay', 'gut'],
    3: ['Frage', 'hilfe', 'unterstuetzung', 'anfrage'],
    4: ['Begruessung', 'hallo', 'hi', 'willkommen', 'moin'],
    5: ['Emotes', 'gronkhDU', 'gronkhHI', 'DinoDance', 'hypeE', 'catJAM', 'blobDance', 'phunkRave', 'BabyRave', 'hypE'],
    6: ['Links', 'https://'],
    7: ['Bekleidung', 'BLUSE', 'hut', 'tshirt', 't-shirt', 'shirt', 'hose']
}

# Initialize an empty list for assigned labels
assigned_labels = []

# Assign labels to clusters based on keyword matching
for message in cleaned_messages:
    assigned = False  # Flag to check if a label is assigned
    for cluster_id, keywords in cluster_keywords.items():
        if any(keyword in message for keyword in keywords):
            assigned_labels.append(cluster_id)
            assigned = True  # Set the flag to indicate a label is assigned
            break

    # Check if a label was assigned to each message, assign to a default label if not
    if not assigned:
        assigned_labels.append(-1)  # Assign to a default or "unknown" cluster

# Save assigned labels to a separate text file
with open('assigned_labels.txt', 'w', encoding='utf-8') as label_file:
    for label in assigned_labels:
        label_file.write(str(label) + '\n')

# Print the messages in each cluster along with assigned labels
for cluster_id in range(num_clusters):
    cluster_messages = [cleaned_messages[i] for i, label in enumerate(assigned_labels) if label == cluster_id]
    cluster_assigned_labels = [assigned_labels[i] for i, label in enumerate(assigned_labels) if label == cluster_id]
    print(f"Cluster {cluster_id + 1} Messages (Assigned Labels: {cluster_assigned_labels}):")
    for message in cluster_messages:
        print(message)
    print("\n")

# Debugging: Print messages that were not assigned a label
unassigned_messages = [cleaned_messages[i] for i, label in enumerate(assigned_labels) if label == -1]
#print("Messages with no assigned label:")
for message in unassigned_messages:
    print(message)
