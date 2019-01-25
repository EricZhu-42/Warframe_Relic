def get_sentence(output):
    if not output: return '输入错误！'
    sentence = ''
    
    for i in range(len(output)):
        if output[i]['valid']:
            sentence += str(i+1) + '：“%(name)s”价值%(ducats)s杜卡德金币，均价%(advicePrice)s白金。' % output[i]
        else:
            sentence += str(i+1) + '：无人售卖或不可交易。'
        sentence += '\n'
    return sentence[:-2]