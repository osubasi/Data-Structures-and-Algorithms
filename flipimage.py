def flipAndInvertImage(image):
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                t = image[i][j]
                image[i][j] = image[i][n - j - 1]
                image[i][n - j - 1] = t
            
            for j in range(n):
                image[i][j] ^= 1

        return image
