## EMSE - R3

# Load required libraries
library(car)  # For VIF calculation

# Read data from a CSV file
Orgdata <- read.csv("/Users/narjes/Documents/ETS/Contrib4-CodeReview/R2/MRA.csv")

head(Orgdata)


# Define a function to filter out the top 3% of outliers
remove_outliers <- function(Orgdata, percentile = 0.03) {
  # Create a copy of the dataset to avoid overwriting
  filtered_data <- Orgdata
  
  # Loop through each numeric variable in the dataset
  for (col_name in colnames(filtered_data)) {
    if (is.numeric(filtered_data[[col_name]])) {
      # Calculate the upper cutoff (97th percentile)
      upper_cutoff <- quantile(filtered_data[[col_name]], probs = 1 - percentile, na.rm = TRUE)
      
      # Filter the data to exclude values above the cutoff
      filtered_data <- filtered_data[filtered_data[[col_name]] <= upper_cutoff, ]
    }
  }
  return(filtered_data)
}

# Apply the function to my dataset
data <- remove_outliers(Orgdata, percentile = 0.03)

# Verify the changes
summary(filtered_data)



# Log-transform predictors 
data$log_Cycle <- log(data$cycle + 1)
data$log_Age <- log(data$age + 1)
data$log_Size <- log(data$size + 1)

data$Type <- as.factor(data$type)
data_iac <- subset(data, Type == "IaC")
data_noniac <- subset(data, Type == "Non-IaC")
#iac model
model_iac <- lm(description ~  log_Size+ log_Age +log_Cycle , data = data_iac)

vif(model_iac)
summary(model_iac)
#non-iac model
model_noniac <- lm(description ~ log_Size+ log_Age +log_Cycle, data = data_noniac)
vif(model_noniac)
summary(model_noniac)


#sum squares

anova_results_iac <- Anova(model_iac, type = "II")
#print(anova_results_iac)
ss_values <- anova_results_iac$`Sum Sq`
total_ss <- sum(ss_values)
percentage_contrib <- (ss_values / total_ss) * 100
anova_results_iac$Percentage <- round(percentage_contrib, 3)
print(anova_results_iac)

anova_results_noniac <- Anova(model_noniac, type = "2")
#print(anova_results_noniac)
nss_values <- anova_results_noniac$`Sum Sq`
ntotal_ss <- sum(nss_values)
npercentage_contrib <- (nss_values / ntotal_ss) * 100
anova_results_noniac$Percentage <- round(npercentage_contrib, 3)
print(anova_results_noniac)


sd_iac <- sd(data_iac$period, na.rm = TRUE)
sd_noniac <- sd(data_noniac$period, na.rm = TRUE)

cat("Standard Deviation :", sd_iac, "\n")
cat("Standard Deviation :", sd_noniac, "\n")

