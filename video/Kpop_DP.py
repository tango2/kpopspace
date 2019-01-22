import json,re,csv
def write_csv_header(output):
    writer = csv.writer(output)
    writer.writerow(["index", "frame_number", "number_of_parts","group_id"])
output_file = "output.csv"

with open(output_file, "wb") as output:
    writer = csv.writer(output)
    write_csv_header(output)
    with open("black_pink_dp_figures.json") as f:
        lines = f.readlines()
        count = 0
        frame_group = 0
        previous_frame =""
        temp_data = []
        for idx, val in enumerate(lines):
            frame_number_value = ""
            delimited_line = val.split("boxes")
            frame_number_raw = delimited_line[0]
            frame_number_regex = re.search(r"[0-9]+.[0-9]+", frame_number_raw) # get the frame_number
            if frame_number_regex:
                frame_number = frame_number_regex.group(0)
                frame_number_value = frame_number
            #frame_number = frame_number_raw.replace()
        # print len(delimited_line)
            if len(delimited_line) == 2:
                boxes_raw = delimited_line[1].split("outlines")[0]
                bodies = boxes_raw.count('[') - 1 # get the bodies
                part_check = val.split("keypoints")            
                # count the parts
                number_parts = len(part_check)   
                # if there is 1 body and more than 7 parts...
                if number_parts == 2: 
                    bodyparts_raw = part_check[1]
                    number_parts = bodyparts_raw.count('[') - 1  
                print number_parts
                if bodies == 1 and number_parts > 7:
                    # add the data                      
                    out_data = [idx,frame_number_value,number_parts,frame_group]
                    # put it into the temp data
                    temp_data.append(out_data)
                    # if a previous frame exists...
                    if previous_frame != "":  
                        # then check the previous frame with this one for consecutiveness
                        if previous_frame + 1 == idx:
                            #if this is consecutive... add 1 to the count
                            count +=1
                            # if cant find.. then checks to see how many consecutive count is there 
                else:
                    # if the count is not 0...
                    if count != 0:
                        # and if the count is greater than 12...
                        if count > 12:
                            # write our temp data!
                            writer.writerows(temp_data)
                            ## OPTIONAL: let us know how many consecutive there is ##
                            print "# consecutive: ", str(count)
                            print "group id: ", str(frame_group)
                            ## END OPTIONAL ##
                        # reset the count
                        count = 0
                        # increment the frame group
                        frame_group += 1
                    # clear the temp_data    
                    temp_data=[]
                # set the previous frame variable to this current idx value    
                previous_frame = idx
print "script complete"
# close the file
f.close()
output.close()

#For each line, count the number of parts and if parts is greater than "two" (because if no parts returns as 1), exclude it - done

# if parts is repeated in a frame, exclude it - done
# if remaining frames have more than 8 coordiantes (DONE) 
# check following frame that have more than 8 coordinates - DONE
    #we need to find a way to check lines consecutively - DONE
    #create a list of frames that are ahead of the current frame and check if this frame follows in that list DONE
# add to output if 13 consecutive frames with more than 8 coordinates are found DONE