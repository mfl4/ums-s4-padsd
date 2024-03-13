def jumlah_huruf_konsonan(kata):
    i = 0
    for huruf in kata:
        if huruf.lower() not in 'aiueo':
            i += 1
    return len(kata), i

print(jumlah_huruf_konsonan('Surakarta'))
print(jumlah_huruf_konsonan('FARHAN'))
