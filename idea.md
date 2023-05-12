# Basic implementation idea

## Encode

1. Take a URL
2. Check if it is present in the "database" (optional)
3. If yes, return (optional)
4. If no (optional), increment the current counter
5. Transform counter f.e. to base60
6. Store counter as key, link as value in the "database"

## Decode

1. Take a URL
2. Check if it is present in the "database" as key
3. If yes return according value
4. If not, return Error
