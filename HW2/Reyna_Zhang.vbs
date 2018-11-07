
        
Sub getTickerName()
    Dim mostInTicker, mostDeTicker, mostVoTicker As String
    Dim mostInValue, mostDeValue, mostVolume As Double

    For Each ws In Worksheets
        numRow = ws.UsedRange.Rows.Count
 
        ws.Cells(1, 9).Value = "Ticker"
        ws.Cells(1, 10).Value = "Yearly Change"
        ws.Cells(1, 11).Value = "Percent Change"
        ws.Cells(1, 12).Value = "Tot Stock Volume"
        Dim yearOpenValue As Double
        Dim yearEndValue As Double
        
        Dim total As Double
        Dim tickerRow As Integer
        total = 0
        tickerRow = 2
        yearOpenValue = ws.Cells(2, "C")
        total = ws.Cells(2, "G")
    
        For i = 3 To numRow
            If ws.Cells(i, 1).Value <> ws.Cells(i - 1, 1).Value Then 'IF HITTING THE NEW TICKER
                'GET THE LAST TICKER'S NAME
                ws.Cells(tickerRow, "I") = ws.Cells(i - 1, 1).Value
                'GET THE LAST TICKER'S TOTAL VOLUM
                ws.Cells(tickerRow, "L") = total
                'get the year end ticker value
                yearEndValue = ws.Cells(i - 1, "F")
                'write this ticker's yearly
                ws.Cells(tickerRow, "J") = yearEndValue - yearOpenValue
                If ws.Cells(tickerRow, "J") > 0 Then
                    ws.Cells(tickerRow, "J").Interior.Color = vbGreen
                Else
                    ws.Cells(tickerRow, "J").Interior.Color = vbRed
                End If
                'write percentage change
                If yearOpenValue = 0 Then
                    ws.Cells(tickerRow, "K") = 0
                Else
                    ws.Cells(tickerRow, "K") = ws.Cells(tickerRow, "J") / yearOpenValue
                End If
                ws.Cells(tickerRow, "K").Style = "Percent"
                
                'reset yearOpenValue and total to new ticker
                total = 0
                yearOpenValue = ws.Cells(i, "C")

                tickerRow = tickerRow + 1
            End If
            total = total + ws.Cells(i, "G").Value
        Next i
    
        '' hard part - first define the header
        ws.Cells(2, "O").Value = "Greatest % Increase"
        ws.Cells(3, "O").Value = "Greatest % Decrease"
        ws.Cells(4, "O").Value = "Greatest Total Volume"
        ws.Cells(1, "P").Value = "Ticker"
        ws.Cells(1, "Q").Value = "Value"
        
        '' initialize greatest values
        mostInValue = -1
        mostDeValue = 1
        mostVolume = 0
        For j = 2 To tickerRow
            If ws.Cells(j, "K").Value > mostInValue Then
                mostInValue = ws.Cells(j, "K")
                mostInTicker = ws.Cells(j, "I")
            ElseIf ws.Cells(j, "K").Value < mostDeValue Then
                mostDeValue = ws.Cells(j, "K")
                mostDeTicker = ws.Cells(j, "I")
            End If
            If ws.Cells(j, "L").Value > mostVolume Then
                mostVolume = ws.Cells(j, "L")
                mostVoTicker = ws.Cells(j, "I")
            End If
        Next j
        ws.Cells(2, "P") = mostInTicker
        ws.Cells(2, "Q") = mostInValue
        ws.Cells(2, "Q").Style = "Percent"
        
        ws.Cells(3, "P") = mostDeTicker
        ws.Cells(3, "Q") = mostDeValue
        ws.Cells(3, "Q").Style = "Percent"
        
        ws.Cells(4, "P") = mostVoTicker
        ws.Cells(4, "Q") = mostVolume
    
    Next ws
    
    
    

End Sub


 '
'End Function

