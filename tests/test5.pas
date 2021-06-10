program PowersofTwo;
var
   numperline : integer;
   maxnum : integer;
   base : integer;
   number : integer;
   linecount : integer;

begin
   numperline := 5;
   maxnum := 20000;
   base := 2;
   write('Powers of ', base, ', 1 <= x <= ', maxnum, ':');
   number := 1;
   linecount := 0;
   while number <= maxnum do
      begin
         linecount := linecount + 1;
         if linecount > 1 then
         begin
            write (', ');
         end;
         write (number);
         if (linecount = numperline) and not (number * 2 > maxnum) then
            begin
               write(',\n');
               linecount := 0;
            end;
         number := number * base;
      end;
   write('\n');

end.