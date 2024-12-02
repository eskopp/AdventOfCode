% AoC 2024 - Day 2 - Task 1
% https:%erik-skopp.de/AdventofCode/2024/2/
% https:%github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_1.m
%
% Day 2 - Red-Nosed Reports
% result: 306

% Load data from the input file
fileID = fopen('example.in', 'r');
data = textscan(fileID, '%s', 'Delimiter', '\n');
fclose(fileID);

% Convert data into a cell array of numeric arrays
data = cellfun(@(x) str2double(strsplit(x)), data{1}, 'UniformOutput', false);

% Function to check if a report is safe
is_safe = @(levels) ...
    (issorted(levels) || issorted(levels, 'descend')) && ...
    all(abs(diff(levels)) >= 1 & abs(diff(levels)) <= 3);

% Count the number of safe reports
safe_count = sum(cellfun(is_safe, data));

% Display the result
fprintf('Number of safe reports: %d\n', safe_count);
