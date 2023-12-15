library(dplyr)


desired_sample_size <- 379


data<- read.csv("IAC-CodeReviews.csv")


unique_samples <- data %>%
  group_by(Phase) %>%
  sample_n(size = 1) %>%
  ungroup()

# Calculate the remaining slots needed
remaining_slots <- desired_sample_size - nrow(unique_samples)

# Calculate the adjusted sampling probabilities
adjusted_probabilities <- table(data$Phase) / sum(table(data$Phase))
adjusted_probabilities


additional_samples <- data %>%
  anti_join(unique_samples, by = "ChangeID") %>%  # Exclude already sampled developers
  sample_n(size = remaining_slots, replace = TRUE, prob = adjusted_probabilities) %>%
  ungroup()

#mysample <- bind_rows(unique_samples, additional_samples)
#mysample

mysample <- bind_rows(unique_samples, additional_samples) %>%
  distinct(ChangeID, .keep_all = TRUE)
mysample

write.csv(mysample,"WeightedSampleR_.csv", row.names = FALSE)

