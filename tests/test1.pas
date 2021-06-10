program TEST;
var
i : integer;
    procedure foo;
    var
     i: integer;
    begin
        i := 1;
    end;
    begin
        while i = 1 do
        begin
            write(i);
        end;
        repeat
            write(i);
            i := i + 1;
        until i = 0;
        for i := 0 to 2 do
        begin
            if i = 1 then
            begin
                i := 0;
            end
            else
            begin
                i := 1;
            end;
        end;
    end.