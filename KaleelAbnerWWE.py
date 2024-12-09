
# Data for the two WWE fighters (John Cena and Roman Reigns)
fighters = ['John Cena', 'Roman Reigns']
wins = [250, 220]  # Example number of wins
losses = [75, 50]  # Example number of losses

# Set positions for the bars on the x-axis
x = np.arange(len(fighters))  # Positions of the fighters

# Width of the bars
width = 0.35  

# Creating the bar chart
fig, ax = plt.subplots()

# Bar charts for wins and losses
ax.bar(x - width/2, wins, width, label='Wins', color='green')
ax.bar(x + width/2, losses, width, label='Losses', color='red')

# Adding titles and labels
ax.set_title('Wins and Losses Comparison: John Cena vs Roman Reigns', fontsize=14)
ax.set_xlabel('Fighter', fontsize=12)
ax.set_ylabel('Number of Matches', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(fighters)

# Adding a legend
ax.legend()

# Show the chart
plt.tight_layout()
plt.show()
