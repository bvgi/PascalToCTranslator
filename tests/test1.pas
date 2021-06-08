program TEST;
    procedure foo;
    begin
        i := 1;
    end;
    begin
        while i = 1 do
        begin
            writeln(i);
        end;
        repeat
        i := i + 1
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