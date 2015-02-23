import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;

public class Solution {

    public static void readFromFile(File fin) throws IOException {
        FileInputStream fis = new FileInputStream(fin);

        BufferedReader br = new BufferedReader(new InputStreamReader(fis));
        
        String s = "";

        double highest = 1;
        double secondHighest = 0;
        double tmp = -1;

        String highestName = "";
        String secondHighestName = "";

        // Ignore first 3 lines
        s = br.readLine();
        s = br.readLine();
        s = br.readLine();

        while ((s = br.readLine()) != null) {
            String[] result = s.split("\\s+");
            tmp = Double.parseDouble(result[4]) * Double.parseDouble(result[6]) / Double.parseDouble(result[2]);
            if (result[2].length() < 5 && tmp > highest) {
                secondHighest = highest;
                secondHighestName = highestName;
                highest = tmp;
                highestName = result[0];
            } else if (result[2].length() < 5 && tmp > secondHighest && tmp < highest) {
                secondHighest = tmp;
                secondHighestName = result[0];
            }
        }

        br.close();

        System.out.println(highestName);
        System.out.println(secondHighestName);
    }

    public static void main(String[] args) throws IOException {
        File fin = new File("realestate.txt");
        readFromFile(fin);
    }

}
