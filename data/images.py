##Nathan Hinton
##This file should not be edited as it has information that if moved will make the program not function
#5

from threading import Thread

def run(imageSets):
    print('loading image set 1...')
    import data.images1
    t1 = Thread(target=data.images1.run, args=(imageSets, ))
    t1.start()

    print('loading image set 2...')
    import data.images2
    t2 = Thread(target=data.images2.run, args=(imageSets, ))
    t2.start()

    print('loading image set 3...')
    import data.images3
    t3 = Thread(target=data.images3.run, args=(imageSets, ))
    t3.start()

    print('loading image set 4...')
    import data.images4
    t4 = Thread(target=data.images4.run, args=(imageSets, ))
    t4.start()
    t1.join()
    return imageSets