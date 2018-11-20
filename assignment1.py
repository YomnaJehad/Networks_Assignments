def xor(a, b):
    output = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            output.append('0')
        else:
            output.append('1')
    return ''.join(output)
def division(data, gen):
    stopmark = len(gen)
    tmp = data[0 : stopmark]
    while stopmark < len(data):
        if tmp[0] == '1':
            tmp = xor(gen, tmp) + data[stopmark]
        else:
            tmp = xor('0'*stopmark, tmp) + data[stopmark]
        stopmark += 1
    if tmp[0] == '1':
        tmp = xor(gen, tmp)
    else:
        tmp = xor('0'*stopmark, tmp)
    result = tmp
    return result

