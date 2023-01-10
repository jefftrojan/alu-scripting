#!/usr/bin/env ruby
input = ARGV[0]
regex = /School/

if input.match(regex)
  puts "School"
else
  puts ""
end

ruby script.rb "School"
