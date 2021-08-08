##Nathan Hinton
##This file should not be edited as it has information that if moved will make the program not function
#5

def run():
    imageSets = []
    
     
    
    print('loading image set 1...')
    import data.images1
    imageSets = data.images1.run(imageSets)

    
    print('loading image set 2...')
    import data.images2
    imageSets = data.images2.run(imageSets)
    return imageSets
    
    print('loading image set 3...')
    import data.images3
    imageSets = data.images3.run(imageSets)

    
    print('loading image set 4...')
    import data.images4
    imageSets = data.images4.run(imageSets)
    return imageSets