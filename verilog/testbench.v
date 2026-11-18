
module testbench;

reg signed [7:0] s0, s1, s2, s3;
wire [1:0] prediction;

cnn_top DUT (
    .score0(s0),
    .score1(s1),
    .score2(s2),
    .score3(s3),
    .prediction(prediction)
);

initial begin
    s0 = 10; s1 = 20; s2 = 5; s3 = 3;
    #10;
    $display("Prediction: %d", prediction);

    s0 = 30; s1 = 10; s2 = 5; s3 = 2;
    #10;
    $display("Prediction: %d", prediction);

    $finish;
end

endmodule
