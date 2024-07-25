from deepface import DeepFace

def check_ID(img_path1, img_path2, model_name='VGG-Face', normalization='VGGFace'):
    '''
    :param img_path1: str, np.array,
    :param img_path2: str, np.array,
    :param model_name: str,
    :param normalization: str
    :return: boolean
    '''
    result = DeepFace.verify(img1_path=img_path1,
                             img2_path=img_path2,
                             model_name=model_name,
                             normalization=normalization,
                             )
    return result
