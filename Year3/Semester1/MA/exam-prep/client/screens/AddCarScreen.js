import React, {useState} from 'react';
import {
    View,
    Text,
    TextInput,
    TouchableOpacity,
    StyleSheet,
    Alert,
    Keyboard,
    TouchableWithoutFeedback,
} from 'react-native';
import axios from 'axios';
import {useNavigation} from "@react-navigation/native";
import {appendLog} from "../log/Logger";

const AddCarScreen = ({route}) => { // todo change name of class
    const navigation = useNavigation();
    const [isLoading, setIsLoading] = useState(false);
    // todo change these variables
    const [name, setName] = useState('');
    const [supplier, setSupplier] = useState('');
    const [details, setDetails] = useState('');
    const [status, setStatus] = useState('');
    const [quantity, setQuantity] = useState('');
    const [type, setType] = useState('');

    //const currentDate = route.params.date;

    const handleSubmit = async () => {
        //todo this one too
        if (!name || !supplier || !details || !status || !quantity || !type) {
            Alert.alert('Error', 'Please fill all fields');
            return;
        }

        try {
            setIsLoading(true);
            await axios.post('http://192.168.1.134:2406/car', {
                name: name,
                supplier: supplier,
                details: details,
                status: status,
                quantity: parseFloat(quantity),
                type: type
            });
            setIsLoading(false);
            Alert.alert('Success', 'Car entry added successfully');
            setName('');
            setSupplier('');
            setDetails('');
            setStatus('');
            setQuantity('');
            navigation.navigate('CarList');
        } catch (error) {
            appendLog('Error adding car entry');
            Alert.alert('Error', 'Failed to add car entry');
        }
    };

    return (
        <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
            <View style={styles.container}>
                {/*TODO Change here*/}
                <Text style={styles.label}>Name:</Text>
                <TextInput style={styles.input} value={name} onChangeText={setName}/>

                <Text style={styles.label}>Supplier:</Text>
                <TextInput style={styles.input} value={supplier} onChangeText={setSupplier}/>



                <Text style={styles.label}>Details:</Text>
                <TextInput style={styles.input} value={details} onChangeText={setDetails}/>

                <Text style={styles.label}>Status:</Text>
                <TextInput style={styles.input} value={status} onChangeText={setStatus}/>

                <Text style={styles.label}>Quantity:</Text>
                <TextInput
                    style={styles.input}
                    value={quantity}
                    onChangeText={setQuantity}
                    keyboardType="numeric"
                />

                <Text style={styles.label}>Type:</Text>
                <TextInput style={styles.input} value={type} onChangeText={setType}/>

                <TouchableOpacity style={styles.button} onPress={handleSubmit}>
                    <Text style={styles.buttonText}>Add Entry</Text>
                </TouchableOpacity>
            </View>
        </TouchableWithoutFeedback>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        backgroundColor: '#f0f0f0',
    },
    label: {
        fontSize: 18,
        color: '#333',
        marginBottom: 6,
    },
    input: {
        backgroundColor: '#fff',
        paddingHorizontal: 15,
        paddingVertical: 10,
        borderRadius: 4,
        marginBottom: 15,
        borderWidth: 1,
        borderColor: '#ddd',
    },
    button: {
        backgroundColor: '#007AFF',
        padding: 15,
        borderRadius: 4,
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: 10,
    },
    buttonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    },
});
// TODO HERE
export default AddCarScreen;