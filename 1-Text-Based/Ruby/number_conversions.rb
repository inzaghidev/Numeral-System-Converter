def re_val(num)
    if num >= 0 && num <= 9
        return (num + '0'.ord).chr
    else
        return (num - 10 + 'A'.ord).chr
    end
end

def strev(str)
    len = str.length
    (len / 2).times do |i|
        temp = str[i]
        str[i] = str[len - i - 1]
        str[len - i - 1] = temp
    end
end

def from_deci(base, input_num)
    res = ''
    while input_num > 0
        res += re_val(input_num % base)
        input_num = input_num / base
    end
    res.reverse
end

puts 'Konversi Sistem Bilangan dari Desimal'
puts 'Number Base System Converter from Decimal'
puts '==========================================='
print 'Input Number : '
input_num = gets.chomp.to_i
print 'Input Base   : '
base = gets.chomp.to_i
result = from_deci(base, input_num)
puts "#{input_num}[#{base}] = #{result}"