% AoC 2024 - Day 2 - Task 2
% https:%erik-skopp.de/AdventofCode/2024/2/
% https:%github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.m
%
% Day 2 - Red-Nosed Reports
% result: 366

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

% Function to check if a report can be made safe by removing one level
can_be_made_safe = @(levels) any(arrayfun(@(i) ...
    is_safe([levels(1:i-1), levels(i+1:end)]), 1:length(levels)));

% Count the number of safe reports (including Problem Dampener)
safe_count = sum(cellfun(@(report) is_safe(report) || can_be_made_safe(report), data));

% Display the result
fprintf('Number of safe reports with Problem Dampener: %d\n', safe_count);
