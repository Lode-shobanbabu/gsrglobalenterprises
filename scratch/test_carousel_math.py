# Let's test the math for client carousel
cards_count = 6
# 2 unique cards repeated 3 times: [0, 1, 0, 1, 0, 1]
# single card width = 360, gap = 24 -> stride = 384
# 1 cycle (2 cards) = 2 * 384 = 768
print("Cycle width for 2 cards:", 2 * (360 + 24))
print("Total track width:", 6 * (360 + 24))
