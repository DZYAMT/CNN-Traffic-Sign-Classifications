module max_pool (
    input signed [7:0] a,
    input signed [7:0] b,
    input signed [7:0] c,
    input signed [7:0] d,
    output reg signed [7:0] result
);

always @(*) begin
    result = a;
    if (b > result) result = b;
    if (c > result) result = c;
    if (d > result) result = d;
end

endmodule
