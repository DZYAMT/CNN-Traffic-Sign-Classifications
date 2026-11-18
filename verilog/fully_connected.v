
module fully_connected (
    input signed [7:0] in0,
    input signed [7:0] in1,
    input signed [7:0] in2,
    input signed [7:0] in3,
    output reg [1:0] prediction
);

always @(*) begin
    if (in0 >= in1 && in0 >= in2 && in0 >= in3)
        prediction = 2'd0;
    else if (in1 >= in2 && in1 >= in3)
        prediction = 2'd1;
    else if (in2 >= in3)
        prediction = 2'd2;
    else
        prediction = 2'd3;
end

endmodule
