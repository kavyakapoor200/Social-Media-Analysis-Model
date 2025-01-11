import pandas as pd
import random

# Create a mock dataset
data = {
    'Post_ID': range(1, 301),
    'Post_Type': [random.choice(['Carousel', 'Reel', 'Static']) for _ in range(300)],
    'Likes': [random.randint(50, 500) for _ in range(300)],
    'Comments': [random.randint(5, 100) for _ in range(300)],
    'Shares': [random.randint(1, 50) for _ in range(300)],
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('mock_social_media_data.csv', index=False)
print("Mock dataset saved as 'mock_social_media_data.csv'")
