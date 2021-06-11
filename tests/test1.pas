program test1;
var
i : integer;
k : integer;
procedure foo;
var
    j: integer;
begin
    j := 1;
    repeat
        write(j);
        j := j + 1;
    until j = 3;
end;
begin
    foo;
    i := 0;
    while i <> 4 do
    begin
        write(i);
        i := i + 1;
    end;
    for k := 0 to 2 do
    begin
        write('Hello');
    end;
    for k := 4 downto 0 do
    begin
        write('World');
    end;
end.