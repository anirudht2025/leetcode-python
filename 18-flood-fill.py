class Solution:
    def floodFill(self, image, sr, sc, color):
        # Store the original color of the starting cell
        original = image[sr][sc]

        # If both colors are the same, no changes are needed
        if original == color:
            return image

        # Get the number of rows and columns
        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Stop if the cell is outside the image
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Stop if the cell doesn't have the original color
            if image[r][c] != original:
                return

            # Change the current cell to the new color
            image[r][c] = color

            # Visit the cell above
            dfs(r - 1, c)

            # Visit the cell below
            dfs(r + 1, c)

            # Visit the cell to the left
            dfs(r, c - 1)

            # Visit the cell to the right
            dfs(r, c + 1)

        # Start filling from the given starting cell
        dfs(sr, sc)

        # Return the updated image
        return image
